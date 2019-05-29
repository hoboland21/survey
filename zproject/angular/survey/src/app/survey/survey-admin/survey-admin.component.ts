import { Component, OnInit } from '@angular/core';
import { StudentService } from '../student.service';
import { IStudent } from '../student';
import { AnswerService } from '../answer.service';
import { IAnswer } from '../answer';

@Component({
  selector: 'app-survey-admin',
  templateUrl: './survey-admin.component.html',
  styleUrls: ['./survey-admin.component.css']
})
export class SurveyAdminComponent implements OnInit {
  studentList: IStudent[];
  answerList: IAnswer[];
  studFiltered = <any>[];
  constructor(
    private surveyService: StudentService,
    private answerService: AnswerService,
  ) { }

  runAnalysis() {
    this.studentList.forEach(
      stud => {
        let result = this.answerList.filter( answer=>  answer.student == stud.id);
        if(result.length) {
          var obj = { 'name': stud.name,  'grade': stud.grade_level, 'lgth': result.length}
          this.studFiltered.push(obj)
        }
    })
  }  

  ngOnInit() {
    this.surveyService.getStudentList().subscribe(
      data => { 
        this.studentList = data
        this.answerService.getAnswers().subscribe(
        data => { 
          this.answerList = data
          this.runAnalysis()
        })
      })
  }

}
