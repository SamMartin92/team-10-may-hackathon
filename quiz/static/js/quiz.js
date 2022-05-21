const form = document.getElementById('.quizForm');

fetch("./quiz.json")
    .then((res) = res.json())
    .then((data) => {
        data.forEach((quiz) => {
            console.log(Object.entries(quiz));
        });
        form.innerHTML += ``;
    })