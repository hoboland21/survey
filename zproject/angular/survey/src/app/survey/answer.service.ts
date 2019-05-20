import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { IAnswer } from './answer';
import { IStudent } from './student';

@Injectable({
  providedIn: 'root'
})

export class AnswerService {
  
  baseUrl = "/webapi" ;
  constructor( private http: HttpClient) { }

  //==================================================
  addStudent(student: IStudent): Observable<IStudent> {

    return this.http
      .post<IStudent>(`${this.baseUrl}/student/`, student,
        {
          headers: new HttpHeaders({
            'Content-Type': 'application/json',
          })
        }).pipe(catchError(this.handleError));

  }

  //==================================================
  addAnswer(answer: IAnswer): Observable<IAnswer> {
    return this.http
      .post<IAnswer>(`${this.baseUrl}/answer/`, answer,
        {
          headers: new HttpHeaders({
            'Content-Type': 'application/json',
          })
        }).pipe(catchError(this.handleError));
  }
//==================================================
  getAnswer(studentId:number): Observable<IAnswer[]> {
    const courseURL = `/webapi/answer/${studentId}/`;
    return this.http.get<IAnswer[]>(courseURL).pipe(
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
