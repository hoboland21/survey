import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey/survey.service';
import { ISurvey } from '../survey/survey';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  surveys:ISurvey[];
  errorMessage = "";
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private surveyService: SurveyService
  ) { }
//-------------------------------
survey(id:number) {
  this._router.navigate(['/main/survey',id]);
}
//-------------------------------
//-------------------------------
//-------------------------------
//-------------------------------
ngOnInit() {
  
    this.surveyService.getSurveyList().subscribe(
      surveys => this.surveys = surveys,
      error => this.errorMessage = <any>error
    );
    
  

  }

}
