import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SurveyService } from '../survey/survey.service';
import { ISurvey } from '../survey/survey';
import { IQuestion } from './question';
import { IStudent } from './student';
import { IAnswer } from './answer';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { controlNameBinding } from '@angular/forms/src/directives/reactive_directives/form_control_name';
import { AnswerService } from './answer.service';

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
  new_rec : IStudent;
  answers: IAnswer[] = [];
  page_number = 0;
  
  errorMessage = '';
 
  constructor(
    private _router:  Router,
    private _route:   ActivatedRoute,
    private surveyService: SurveyService,
    private formBuilder:FormBuilder,
    private answerService: AnswerService, 


  ) { }


  studentForm = this.formBuilder.group({
    test_code:["",[Validators.required]]
  }) 
  pageForward() {
    
    if (this.page_number <= this.questions.length) {
      this.page_number += 1;
    }
  }
  

  write_answers(id) {
    this.answers.forEach(answer => {
      answer.student=id;
      this.answerService.addAnswer(answer).subscribe(
        data => {    console.log("answer",data);   } ,
        error => {
          this.errorMessage= "Failed to create student Component";
        }
      )
    });
  }


  write_survey() {

    this.answerService.addStudent(this.student).subscribe(
      data => {  
        console.log("Data Id", data.id);
        this.write_answers(data.id);  
      } ,
      error => {
        this.errorMessage= "Failed to create student Component";
      }
      // output as an event -- send the student id out to be used
    )

    console.log(this.student);
  }

  start() {
    this.pageForward();
    this.student.test_code = this.studentForm.value["test_code"]
    this.answers = [];
  }

  finish() {
    this.write_survey();
    this.page_number=0;
    this.studentForm.patchValue({test_code: ""})
    this.ngOnInit();
  }

  mark_answer(mark) {
    var answer:IAnswer = {
      student: 0,
      question: this.questions[this.page_number-1].id,
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
      test_code:"",
      created:new Date()
    }
  }

}
