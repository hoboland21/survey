import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ISurvey } from './survey';

@Injectable({
  providedIn: 'root'
})
export class SurveyService {

  constructor( private http: HttpClient) { }

  getSurveyList(): Observable<ISurvey[]> {
    const surveyURL = `/webapi/survey/`;
    return this.http.get<ISurvey[]>(surveyURL)
  }




}
