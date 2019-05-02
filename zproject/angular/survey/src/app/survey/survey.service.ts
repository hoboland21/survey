import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { ISurvey } from './survey';
import { IQuestion } from './question';

@Injectable({
  providedIn: 'root'
})
export class SurveyService {

  constructor( private http: HttpClient) { }
//==================================================
  getSurveyList(): Observable<ISurvey[]> {
    const surveyURL = `/webapi/survey/`;
    return this.http.get<ISurvey[]>(surveyURL).pipe(
      catchError(this.handleError)
    );
  }
//==================================================
  getSurvey(id:number): Observable<ISurvey> {
    const surveyURL = `/webapi/survey/${id}`;
    return this.http.get<ISurvey>(surveyURL).pipe(
      catchError(this.handleError)
    );
  }
//==================================================
  getQuestions(id:number): Observable<IQuestion[]> {
    const surveyURL = `/webapi/question/${id}`;
    return this.http.get<IQuestion[]>(surveyURL).pipe(
      catchError(this.handleError)
    );
  }



//==================================================
  private handleError(err: HttpErrorResponse) {
    // in a real world app, we may send the server to some remote logging infrastructure
    // instead of just logging it to the console
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      errorMessage = `An error occurred: ${err.error.message}`;
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage);
    return throwError(errorMessage);
  }
}
