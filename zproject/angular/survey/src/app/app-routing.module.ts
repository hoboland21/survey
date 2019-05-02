import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CommonModule } from '@angular/common';
import { NotfoundComponent } from './system/notfound/notfound.component';

const routes: Routes = [
    {   path: 'main',
        component: DashboardComponent
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