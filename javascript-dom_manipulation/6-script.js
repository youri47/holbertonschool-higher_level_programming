// On définit l'URL de l'API
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// On utilise fetch pour envoyer la requête
fetch(url)
  .then(response => {
    // On convertit la réponse reçue en format JSON (objet JavaScript)
    return response.json();
  })
  .then(data => {
    // Une fois qu'on a les données, on sélectionne l'élément HTML
    const characterElement = document.querySelector('#character');
    
    // On injecte le nom du personnage (propriété 'name' du JSON) dans la div
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // C'est toujours bien de gérer les erreurs si l'API ne répond pas
    console.error('Erreur lors de la récupération :', error);
  });
