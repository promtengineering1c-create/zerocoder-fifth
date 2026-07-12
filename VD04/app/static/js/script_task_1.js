function updateTime() {
    fetch('/get_time')
    .then(response => response.json()) // Распаковываем ответ в JSON
    .then(data => {
        // Находим элемент по ID и меняем его текст
        document.getElementById('clock').innerText = "Текущее время: " + data.time;
    });
}
setInterval(updateTime, 1000);
