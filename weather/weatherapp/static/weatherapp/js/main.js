const searchbox = document.querySelector(".search-box");
searchbox.addEventListener("keypress", setQuery);

function setQuery(evt) {
  if (evt.keyCode == 13) {
    const url = `http://localhost:8000/${searchbox.value}/`;
    window.location.replace(url);
  }
}