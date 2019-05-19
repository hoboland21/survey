import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CommonModule } from '@angular/common';
import { NotfoundComponent } from './system/notfound/notfound.component';
import { SurveyMasterComponent } from './survey/survey-master/survey-master.component';

const routes: Routes = [
    {   path: 'main',
        component: DashboardComponent
    },
    {   path: 'main/survey/:id',
        component: SurveyMasterComponent

    },
    {   path: '**', 
        component: NotfoundComponent 
    }
];

@NgModule({
    declarations: [],
    imports: [
        CommonModule,
        RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}