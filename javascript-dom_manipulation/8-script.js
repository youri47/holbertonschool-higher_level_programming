// On attend que le DOM soit complètement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', function() {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      // On sélectionne l'élément avec l'ID hello
      const helloElement = document.querySelector('#hello');
      
      // On affiche la valeur de "hello" provenant de l'API
      helloElement.textContent = data.hello;
    })
    .catch(error => console.error('Erreur :', error));
});
