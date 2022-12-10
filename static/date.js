
 var Today = new Date();
 var month = Today.getMonth() + 1;
 var day  = Today.getDate();
 var year = Today.getFullYear();
 if (month < 10)
     month = '0'+ month.toString();
 if (day < 10)
     day = '0' + day.toString();

 var minDate = year + '-' +month +'-'+ day;
 document.getElementbyId('id_check_in').setAttribute(min, minDate);
