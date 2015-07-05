
	function sendHttpPost() {
		

  // Copy the entire URL from <form action>
  var formAction = "https://docs.google.com/forms/d/1_jB9kkBq_pl-eiQhmQNLe2KnDB24jRgBX_PvSRGrFW8/formResponse";

  var payload = {
  //  "entry.149063571": "car",            // type of vehicle
    "entry.1415313175": "xyz",                // name
    "entry.6731709": "red"   //color
  };



  var options = {
    "method": "post",
    "payload": payload
  };

  var response = UrlFetchApp.fetch(formAction, options);
 
}




