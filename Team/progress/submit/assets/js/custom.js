
document.getElementById ("submit_form").onclick = function () {
  var formData = new FormData();

  if (document.getElementsByName ("filevault")[0].files.length > 0) {

    filelist = document.getElementsByName ("filevault")[0].files

    for (var elm in filelist) { 
      if (elm != 'length' && elm != 'item') { 

        formData.append ('file' + elm.toString(), filelist[elm]) 
      } 
    }
  }

  formData.append ("progress", document.getElementsByTagName ("textarea")[0].value)
  

  for(var pair of formData.entries()) {

    console.log(pair[0]+ ', '+ pair[1]); 
  }

$.ajax({

    url: "https://engineering.purdue.edu/477grp19/Team/progress/submit/submit.cgi",

    type: "post",

    processData: false,

    contentType: false,
    data: formData,

    success: function(response){

              alert (response)

              console.log (response)
    },

    error: function (jqXHR, textStatus, errorThrown) {

      alert (textStatus, errorThrown)
    }
  })
}
  
function uploadFile () {

  document.getElementsByName ("filevault")[0].addEventListener ('change', function () { 

    if (document.getElementsByName ("filevault")[0].files.length > 0)
    {

      document.getElementById ("uploader").innerHTML = document.getElementsByName ("filevault")[0].files.length.toString() + " files selected"
    }

    else
    {
      document.getElementById ("uploader").innerHTML = "UPLOAD"
    } 
    })

  document.getElementsByName ('filevault')[0].click()
}