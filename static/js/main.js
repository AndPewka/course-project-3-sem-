let bAddVac = document.querySelector(".bAddVac")
let AddVac = document.querySelector(".AddVac")
let closeVac = document.querySelector(".close")
let delete_lists = document.querySelectorAll(".delete_list")
let pass_del_vac = document.querySelectorAll(".pass_del_vac")
let pass_del_summ = document.querySelectorAll(".pass_del_summ")

for(let delete_list of delete_lists){
  delete_list.onclick = function(){
    if(document.querySelector(".pass_del_vac")){
      delete_list.parentElement.querySelector(".pass_del_vac").style.display="inline"
    }
    if(document.querySelector(".pass_del_summ")){
      delete_list.parentElement.querySelector(".pass_del_summ").style.display="inline"
    }

  }
}

for(let pass of pass_del_vac){
  pass.onclick = function(){
    hash = pass.parentElement.parentElement.parentElement.parentElement.dataset.id
    send("/deleteVac",{"hash" : hash})
    location.href=""

  }
}

for(let pass of pass_del_summ){
  pass.onclick = function(){
    hash = pass.parentElement.parentElement.parentElement.parentElement.dataset.id
    send("/deleteSumm",{"hash" : hash})
    location.href=""
  }
}

bAddVac.onclick = function(){
  AddVac.style.display="block"
}

closeVac.onclick = function(){
  AddVac.style.display="none"

}

async function send(path, dict) {
  var url = "http://localhost";
  url = url + path
  let response = await fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(dict)
  });
  let parsed = await response.json();
  return parsed
}




