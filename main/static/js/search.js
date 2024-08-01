const searchInput = document.querySelector("#search")
const searchDrop = document.querySelector(".search_drop")
searchInput.addEventListener("input", fetchQuery)


function fetchQuery(event) {
//    console.log('1')   //  типа принта на питоне, проверяем работает или нет, когда точ-то вводим в поиск
    if (searchInput.value.length >= 2){
        fetch(`http://127.0.0.1:8000/api/search_product/?brand=${searchInput.value}`)
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data)
            searchDrop.style.display = "block";
            searchDrop.innerHTML = ""
            for (let item of data) {
                searchDrop.innerHTML += `
                <a class='search_drop-item' href='http://127.0.0.1:8000/detail/${item.id}'>
                    <div class='search_drop-item-img'>
                        <img src='${item.image}'>
                    </div>
                    <p class='search_drop-title'>${item.brand.title} ${item.model}</p>
                </a>
                `
            }
            if (data.length === 0){
                searchDrop.innerHTML = `<div class='search_drop-item'>
                <p class='search_drop-title'>По вашему запросу ничего не найдено</p>
                </div>`
            }
        })
    } else{
        searchDrop.style.display = "none";
    }
}