import $ from 'jquery';
import * as Paginate from 'el-pagination/js/el-pagination.js'

$(function(){ 
  window.jQuery = window.$ = $;
  Paginate.endlessPaginate();
})
