import { Component, OnInit, Input, Output } from '@angular/core';

import { AnswerService } from '../answer.service';
import { CourseService } from '../course.service';

import { IAnswer } from '../answer';
import { ICourse } from '../course';


@Component({
  selector: 'app-survey-answer',
  template: `
  <div *ngFor="let c of courses">
    {{c | json }}
  </div>`
})
export class SurveyAnswerComponent implements OnInit {
  @Input() studentId:number;
  answerList:IAnswer[];
  errorMessage="";
  courseList = new Set();
  courses = []
  constructor(
    private answerService: AnswerService, 
    private courseService: CourseService, 
  ) { }

  ngOnInit() {
    this.answerService.getAnswer(this.studentId).subscribe(
      data => {
        data.forEach(answer => this.courseList.add(answer.course) );
        this.courseList.forEach(courseId=> {
          console.log("Course ID",courseId)
          this.courseService.getCourse(courseId).subscribe(
            c => {
              this.courses.push(c)
              console.log("push",c)
            })
        })

      })
  }

}
