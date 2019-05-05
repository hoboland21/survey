import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey/survey.service';
import { ISurvey } from '../survey/survey';
import { IQuestion } from './question';
import { IStudent } from './student';
import { IAnswer } from './answer';
import { conditionallyCreateMapObjectLiteral } from '@angular/compiler/src/render3/view/util';

@Component({
  selector: 'app-survey',
  templateUrl: './survey.component.html',
  styleUrls: ['./survey.component.css']
})
export class SurveyComponent implements OnInit {
  id : number;
  survey : ISurvey;
  questions: IQuestion[];
  current_question: IQuestion;
  studentId = '';
  student = {} as IStudent ;
  answers: IAnswer[] = [];
  page_number = 0;
  
  errorMessage = '';
 
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private surveyService: SurveyService,

  ) { }

  pageForward() {
    
    if (this.page_number < this.questions.length) {
      this.page_number += 1;
      console.log(this.answers)
    }
  }
  mark_answer(mark) {
    var answer:IAnswer = {
      student: this.student.name,
      question: this.questions[this.page_number].id,
      answer: mark
    }
    this.answers.push(answer)
    this.pageForward();

  }

 
  ngOnInit() {
    this.id = Number(this._route.snapshot.paramMap.get('id'));

    this.surveyService.getSurvey(this.id).subscribe(
      survey => {
        this.survey = survey;
      },
      error => this.errorMessage = <any>error
    );
    
    this.surveyService.getQuestions(this.id).subscribe(
      questions => this.questions = questions,
      error => this.errorMessage = <any>error
    );
    
    this.studentId = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);

    this.student = {
      name:this.studentId,
      survey: this.id,
      test_code:"beta",
      created:new Date()
    }
  }

}
