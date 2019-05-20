import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey.service';
import { IQuestion } from '../question';
import { IAnswer } from '../answer';
import { AnswerService } from '../answer.service';
import { IStudent } from '../student';
import { ISurvey } from '../survey';

import { ICourse } from '../course';

@Component({
  selector: 'app-survey',
  templateUrl: './survey.component.html',
  styleUrls: ['./survey.component.css']
})
export class SurveyComponent implements OnInit {
  
  
  @Input()  student:IStudent;
  @Input()  course:ICourse;
  @Output() surveyOut = new EventEmitter();
  
  survey : ISurvey;
  questions: IQuestion[];
  answers: IAnswer[] = [];
  answered: IAnswer[];
  page_number = 0;
  errorMessage = '';
 
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private surveyService: SurveyService,
    private answerService: AnswerService, 
  ) { }
//====================================
  pageForward() {
    if(this.page_number+1 == this.questions.length) {
      this.write_answers();
    } 
    if (this.page_number <= this.questions.length) {
      this.page_number += 1;
    }
  }
//====================================
  write_answers() {
    this.answers.forEach(answer => {
      this.answerService.addAnswer(answer).subscribe(
        data => {    console.log("answer",data);   } ,
        error => {
          this.errorMessage= "Failed to create student Component";
        }
      )
    });
  }
//====================================
  mark_answer(mark) {
    var answer:IAnswer = {
      course: this.course.id,
      student: this.student.id,
      question: this.questions[this.page_number].id,
      answer: mark
    }
    this.answers.push(answer)
    this.pageForward();
  }
//====================================
  next_course() {
    this.surveyOut.emit();
  }
//====================================
  finished() {
    this._router.navigate(['/main']);
  }
//====================================
ngOnInit() {
    this.surveyService.getQuestions(this.student.survey).subscribe(
      questions => this.questions = questions,
      error => this.errorMessage = <any>error
    );
  }
}
