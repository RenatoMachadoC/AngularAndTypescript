import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Content } from './pages/content/content';

const routes: Routes = [

  {

    path:'',
    component: Home

  },
  {

    path:'content',
    component: Content

  },


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
