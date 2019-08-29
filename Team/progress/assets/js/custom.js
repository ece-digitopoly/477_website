document.getElementById ("submit_form").onclick = function () {
$.ajax({
    url: "https://engineering.purdue.edu/477grp19/Team/progress/submit/submit.cgi",
    type: "post",
    datatype: "text",
    data: {progress: document.getElementsByTagName ("textarea")[0].value},
    success: function(response){
              alert (response)
    }
  })
}

function uploadFile () {
  document.getElementsByName ('filevault')[0].click()
  $('td[name=filevault]').change (function () { 
    document.getElementById ("uploader").innerHTML = document.getElementsByName ('filevault')[0].value
  })
}