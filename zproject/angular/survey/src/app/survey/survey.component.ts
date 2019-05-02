import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey/survey.service';
import { ISurvey } from '../survey/survey';
import { IQuestion } from './question';

@Component({
  selector: 'app-survey',
  templateUrl: './survey.component.html',
  styleUrls: ['./survey.component.css']
})
export class SurveyComponent implements OnInit {
  id : number;
  survey : ISurvey;
  questions: IQuestion[];
  errorMessage = '';
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private surveyService: SurveyService
  ) { }

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
