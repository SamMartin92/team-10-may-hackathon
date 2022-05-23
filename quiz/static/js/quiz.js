document.addEventListener("DOMContentLoaded", function () {
    const data = [{
            "question": "A child appears to be lost in the street, do you:",
            "options": [{
                    "option": "Look up and down the street for their parents",
                    "type": "Positive Self Esteem",
                    "points": 1
                },
                {
                    "option": "Stay with them until they are collected",
                    "type": "Sense of Belonging",
                    "points": 1
                },
                {
                    "option": "Blog on social media to find a search party",
                    "type": "Sense of Purpose",
                    "points": 1
                },
                {
                    "option": "Re-assure they will find their parents",
                    "type": "Positive Outlook",
                    "points": 1
                },
                {
                    "option": "Call local services",
                    "type": "Autonomy",
                    "points": 1
                }
            ]
        },
        {
            "question": "You see a retired man attending to his garden, you are likely to:",
            "options": [{
                "option": "Check back later to see it's progress",
                "type": "Positive Self Esteem",
                "points": 1
            }, {
                "option": "Gift them with a plant from the local shop",
                "type": "Sense of Belonging",
                "points": 1
            }, {
                "option": "Ask if they would like help",
                "type": "Sense of Purpose",
                "points": 1
            }, {
                "option": "Compliment on their work",
                "type": "Positive Outlook",
                "points": 1
            }, {
                "option": "Advise some nice flower shops and idea's",
                "type": "Autonomy",
                "points": 1
            }]
        },
        {
            "question": "A car has broken down on your street, would you:",
            "options": [{
                "option": "Watch as they fix the car",
                "type": "Positive Self Esteem",
                "points": 1
            }, {
                "option": "Offer to use your drive to get them off the road",
                "type": "Sense of Belonging",
                "points": 1
            }, {
                "option": "Check if they need help",
                "type": "Sense of Purpose",
                "points": 1
            }, {
                "option": "Avoid making a fuss of them, they will fix it",
                "type": "Positive Outlook",
                "points": 1
            }, {
                "option": "Guide them to move the car to a safer place",
                "type": "Autonomy",
                "points": 1
            }]
        },
        {
            "question": "Your friend needs to borrow some money, the best action is to:",
            "options": [{
                "option": "Give them a list of chores, offering money on completion",
                "type": "Positive Self Esteem",
                "points": 1
            }, {
                "option": "Offer them the money",
                "type": "Sense of Belonging",
                "points": 1
            }, {
                "option": "Talk them through their expenses",
                "type": "Sense of Purpose",
                "points": 1
            }, {
                "option": "Talk about the situation and how to go forward",
                "type": "Positive Outlook",
                "points": 1
            }, {
                "option": "Suggest contact for help and actions",
                "type": "Autonomy",
                "points": 1
            }]
        },
        {
            "question": "Living next door to a charity shop, you:",
            "options": [{
                "option": "Offer help in the evening",
                "type": "Positive Self Esteem",
                "points": 1
            }, {
                "option": "Look to donate items on a regular basis",
                "type": "Sense of Belonging",
                "points": 1
            }, {
                "option": "Promote the shop to your contacts",
                "type": "Sense of Purpose",
                "points": 1
            }, {
                "option": "Aim to buy from there frequently",
                "type": "Positive Outlook",
                "points": 1
            }, {
                "option": "Make suggestions to improve the shop",
                "type": "Autonomy",
                "points": 1
            }]
        }
    ];

    const suggestions = {
        "Positive Self Esteem": ["Talking with some-one at least once a day, could be Friends, Family or even Colleagues. Adding structure by setting the time aside to create this will also support, i.e calling around lunch time.", "Look to become a volunteer at school, charity, hospital and more! (Check with local goverment websites)", "Do not become too reliant on technology or social media's. This creates a fixation of only communicating by texting, messaging or e-mail. Seeing people face to face can include that support you are missing!"],
        "Sense of Belonging": ["Becoming pysyically active increase your self-esteem, helps oyu set goals or challengces and causes chemical changes in your brain to help the positive outlook.", "Don't just sign up for a gym then push yourself to go, find a sport or activity you enjoy and take part. i.e, you will find a 30 minute session is more of a challenge rather than swimming 5 laps of the local swimming pool."],
        "Sense of Purpose": ["Focusing on learning of a new skill promotes self-confidence and self-esteem. Also provides a sense of purpose and a new topic for conversations.", "Youtube, How-To websites and free courses are avaialble for a range of skills to be learnt. From D.I.Y to Cooking, Art/Drawing and Coding.", "Make sure you pick a topic of interest, do not feel pressured into requirement of new qualifications or exams."],
        "Positive Outlook": ["Giving to others provides a feeling of purpose and self-worth, boosting your positive feeling and sense of reward.", "This does not always include deparing with an item of value, a large contribution is your effort. These include following with expressing your thanks, spending time with your peers, Offering help with your knowledge of the specific topic they are working on, volunteering at local organisations."],
        "Autonomy": ["Don't get overwhelmed with what has happened and about to happen", "Take a step back, or an outside table at a coffee shop and observe", "Look for objects to appreciate, Health, Time, Patience, the weather."]
    }

    const form = document.getElementById('quizForm');
    const resultsSection = document.getElementById('resultsSection');

    data.forEach((quiz, quizIdx) => {
        form.innerHTML += `
            <div class="question my-5">
                <h3>${quiz.question}</h3>
            </div>
        `;

        form.innerHTML += `
            <div class="answers p-5 text-center">
                ${quiz.options.map((option, opIdx) => `
                    <input type="radio" id="q${quizIdx}_${opIdx}" name="q${quizIdx}" value="${opIdx}"> <label for="q${quizIdx}_${opIdx}">${option.option}</label><br />
                `).join('')}
            </div>
        `;
    });

    form.innerHTML += `
        <div id="linkDown" class="my-5"></div>
        <div id="quizBtns" class="my-5">
            <input type="reset" value="Restart"/><br>
            <input id="submitQuiz" type="submit" value="Submit"/>
        </div>
    `;

    const linkDown = document.getElementById('linkDown');

    const highestValues = [];

    const highestResults = (results = {}) => {
        const sortedResults = Object.entries(results).sort((a, b) => b[1] - a[1]);

        const firstKey = sortedResults[0][0];
        const firstVal = sortedResults[0][1];
        const secondKey = sortedResults[1][0];
        const secondVal = sortedResults[1][1];
        const thirdVal = sortedResults[2][1];

        if (firstVal > secondVal) {
            highestValues.push({
                [firstKey]: firstVal
            });
        } else if (firstVal === secondVal && firstVal !== thirdVal) {
            highestValues.push({
                [firstKey]: firstVal
            }, {
                [secondKey]: secondVal
            });
        } else {
            highestValues.push("All Equal");
        }

        return highestValues
    }
    let finalResults = [];

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        linkDown.innerHTML += '<h4 class="text-success">See results below!</h4>';
        let positive_self_esteem = 0
        let sense_of_belonging = 0;
        let sense_of_purpose = 0;
        let positive_outlook = 0;
        let autonomy = 0;

        data.forEach((quiz, quizIdx) => {
            quiz.options.forEach((option, opIdx) => {
                const input = document.getElementById(`q${quizIdx}_${opIdx}`);
                if (input.checked && input.nextElementSibling.innerHTML === option.option) {
                    switch (option.type) {
                        case "Positive Self Esteem":
                            positive_self_esteem++;
                            break;
                        case "Sense of Belonging":
                            sense_of_belonging++;
                            break;
                        case "Sense of Purpose":
                            sense_of_purpose++;
                            break;
                        case "Positive Outlook":
                            positive_outlook++;
                            break;
                        case "Autonomy":
                            autonomy++;
                            break;
                    }
                }
            });
        });

        const allResults = {
            "Positive Self Esteem": positive_self_esteem,
            "Sense of Belonging": sense_of_belonging,
            "Sense of Purpose": sense_of_purpose,
            "Positive Outlook": positive_outlook,
            "Autonomy": autonomy
        }

        const getFinalQuizResults = (highestResults = () => {}) => {
            highestResults.map((res) => {
                Object.values(res).join().replaceAll(',', '') === "All Equal" ?
                    finalResults.push("You have a balanced mindset!") :
                    finalResults.push(Object.keys(res)[0]);
            });
        }
        getFinalQuizResults(highestResults(allResults))
        finalResults.forEach((res) => form.innerHTML += `<p><strong>Type:</strong> ${res}</p>`);

        Object.entries(suggestions).forEach((value, key) => {
            if (finalResults.includes(value[0])) {
                resultsSection.innerHTML += `<h3 class="mt-5">${value[0]}</h3>`;
                value[1].forEach((v) => resultsSection.innerHTML += `<li>${v}</li>`)
            }
        });
        const quizBtns = document.getElementById('quizBtns');
        quizBtns.style.display = 'none';
    });
});