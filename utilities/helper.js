function suggestDishes() {
    let inputField = document.querySelector("#user-instructions");
    let suggestionsBox = document.querySelector("#suggestions");
  
    inputField.addEventListener("input", function () {
      let userInput = inputField.value.trim();
  
      if (userInput.length < 2) {
        suggestionsBox.innerHTML = "";
        return;
      }
  
      let apiUrl = `https://api.mockfood.com/suggestions?q=${userInput}`;
  
      axios.get(apiUrl).then((response) => {
        let suggestions = response.data.suggestions;
        let suggestionHTML = suggestions
          .map((dish) => `<li onclick="selectDish('${dish}')">${dish}</li>`)
          .join("");
  
        suggestionsBox.innerHTML = `<ul>${suggestionHTML}</ul>`;
      });
    });
  }
  
  function selectDish(dishName) {
    document.querySelector("#user-instructions").value = dishName;
    document.querySelector("#suggestions").innerHTML = "";
  }
  
  suggestDishes();

  

  function showLoadingEffect(recipeName) {
    let recipeElement = document.querySelector("#recipe");
    let dots = 0;
  
    recipeElement.innerHTML = `<div class="blink">👩🏽‍🍳 Generating ${recipeName} recipe</div>`;
  
    let interval = setInterval(() => {
      dots = (dots + 1) % 4;
      recipeElement.innerHTML = `<div class="blink">👩🏽‍🍳 Generating ${recipeName} recipe${".".repeat(dots)}</div>`;
    }, 500);
  
    return interval;
  }
  
  function generateRecipe(event) {
    event.preventDefault();
    let instructions = document.querySelector("#user-instructions").value;
    let apiKey = "16t1b3fa04b8866116ccceb0d2do3a04";
    let apiUrl = `https://api.shecodes.io/ai/v1/generate?prompt=${instructions}&key=${apiKey}`;
  
    let loadingInterval = showLoadingEffect(instructions);
  
    axios.get(apiUrl).then((response) => {
      clearInterval(loadingInterval);
      document.querySelector("#recipe").innerHTML = response.data.answer;
    });
  }
  
  document.querySelector("#recipe-generator-form").addEventListener("submit", generateRecipe);

  
  