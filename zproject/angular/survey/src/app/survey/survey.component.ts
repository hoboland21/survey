import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey/survey.service';
import { ISurvey } from '../survey/survey';
import { IQuestion } from './question';
import { IStudent } from './student';
import { IAnswer } from './answer';

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
  student: IStudent;
  answers: IAnswer[];
  page_number = 0;

  errorMessage = '';
 
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private formBuilder: FormBuilder,
    private surveyService: SurveyService
  ) { }
  answerForm : FormGroup;
  pageForward() {
    
    if (this.page_number < this.questions.length) {
      this.page_number += 1;
    }
  }

  
  ngOnInit() {
    this.id = Number(this._route.snapshot.paramMap.get('id'));
    
    this.surveyService.getSurvey(this.id).subscribe(
      survey => this.survey = survey,
      error => this.errorMessage = <any>error
    );
    
    this.surveyService.getQuestions(this.id).subscribe(
      questions => this.questions = questions,
      error => this.errorMessage = <any>error
    );
    
  }

}
