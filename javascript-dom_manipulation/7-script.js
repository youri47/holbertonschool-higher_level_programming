// URL pour récupérer tous les films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    // La liste des films se trouve dans la propriété 'results' qui est un tableau
    const movies = data.results;
    const listElement = document.querySelector('#list_movies');

    // On boucle sur chaque film du tableau
    movies.forEach(movie => {
      // Pour chaque film, on crée un nouvel élément <li>
      const listItem = document.createElement('li');
      
      // On lui donne le titre du film comme contenu
      listItem.textContent = movie.title;
      
      // On l'ajoute à notre liste <ul>
      listElement.appendChild(listItem);
    });
  })
  .catch(error => console.error('Erreur :', error));
