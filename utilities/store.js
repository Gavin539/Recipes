function saveRecipe() {
    let recipeContent = document.querySelector("#recipe").innerHTML;
    let recipeName = document.querySelector("#user-instructions").value;
  
    if (!recipeContent || !recipeName) {
      alert("No recipe to save!");
      return;
    }
  
    let savedRecipes = JSON.parse(localStorage.getItem("recipes")) || {};
    savedRecipes[recipeName] = recipeContent;
    localStorage.setItem("recipes", JSON.stringify(savedRecipes));
  
    alert(`Recipe for ${recipeName} saved!`);
  }
  
  function loadSavedRecipes() {
    let savedRecipes = JSON.parse(localStorage.getItem("recipes")) || {};
    let recipeList = document.querySelector("#saved-recipes");
  
    if (Object.keys(savedRecipes).length === 0) {
      recipeList.innerHTML = "<p>No saved recipes yet.</p>";
      return;
    }
  
    let recipeHTML = Object.keys(savedRecipes)
      .map((name) => `<li onclick="displaySavedRecipe('${name}')">${name}</li>`)
      .join("");
  
    recipeList.innerHTML = `<ul>${recipeHTML}</ul>`;
  }
  
  function displaySavedRecipe(recipeName) {
    let savedRecipes = JSON.parse(localStorage.getItem("recipes"));
    document.querySelector("#recipe").innerHTML = savedRecipes[recipeName];
  }
  
  document.querySelector("#save-button").addEventListener("click", saveRecipe);
  document.addEventListener("DOMContentLoaded", loadSavedRecipes);

  
  function startVoiceRecognition() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    let inputField = document.querySelector("#user-instructions");
  
    recognition.start();
  
    recognition.onresult = function (event) {
      let speechResult = event.results[0][0].transcript;
      inputField.value = speechResult;
      console.log("User said: ", speechResult);
    };
  
    recognition.onerror = function (event) {
      console.error("Speech recognition error", event.error);
      alert("Sorry, could not recognize your voice.");
    };
  
    recognition.onend = function () {
      console.log("Speech recognition ended.");
    };
  }
  
  document.querySelector("#voice-button").addEventListener("click", startVoiceRecognition);
  