import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { ICourse } from './course';

@Injectable({
  providedIn: 'root'
})

export class CourseService {
  


  constructor( private http: HttpClient) { }
//==================================================
getCourseList(): Observable<ICourse[]> {
  const courseURL = `/webapi/course/`;
  return this.http.get<ICourse[]>(courseURL).pipe(
    catchError(this.handleError)
  );
}
//==================================================
getCourse(id:number): Observable<ICourse> {
  const courseURL = `/webapi/course/${id}/`;
  return this.http.get<ICourse>(courseURL).pipe(
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
