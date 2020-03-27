import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/views/HelloWorld'
import Home from '@/views/Home'
import About from '@/views/About'
import TableViewer from '@/views/TableViewer'
import TestTable from '@/views/TestTable'
import ImageTable from '@/views/ImageTable'
import RawAPI from '@/views/RawAPI'
import NotFound from '@/views/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {path: '/', name: 'HelloWorld', component: HelloWorld},
    {path: '/home', name: 'Home', component: Home},
    {path: '/about', name: 'About', component: About},
    {path: '/table', name: 'Table', component: TableViewer, meta:{keepAlive: true}},
    {path: '/test_table', name: 'TestTable', component: TestTable},
    {path: '/image_table', name: 'ImageTable', component: ImageTable},
    {path: '/api', name: 'API', component: RawAPI},
    {path: '*', name: 'NotFound', component: NotFound},
  ]
})
