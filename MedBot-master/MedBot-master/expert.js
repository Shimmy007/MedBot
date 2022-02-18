var ExpertSystem;

function checkLocalStorage() {
    try {
        return 'localStorage' in window && window['localStorage'] !== null && localStorage != undefined;
    } catch (e) {
        return false;
    }
}

function loadItemsFromLocalStorage() {
    if (!checkLocalStorage()) {
        return;
    }
    var template = '<div class="b_page_test_switch__item b_page border_radius" index="{1}">{0}</div>';
    var target = $(".b_page_test_switch");

    for (var i = 0; localStorage["ExpertSys" + i]; i++) {
        target.html(target.html() + template.replace("{1}", "ExpertSys" + i).replace("{0}", JSON.parse(localStorage["ExpertSys" + i]).title));

    }
}

function loadFromLocalStorage(localStorageIndex) {
    return new Test(JSON.parse(localStorage[localStorageIndex]));
}

function saveToLocalStorage(test) {
    if (!checkLocalStorage()) {
        return;
    }
    for (var i = 0; localStorage[i]; i++) {
        if (localStorage["ExpertSys" + i].match(test.title)) {
            localStorage.setItem("ExpertSys" + i, test.stringify());
            return;
        }
    }
    localStorage.setItem("ExpertSys" + i, test.stringify());
}

function step() {
    //var ans = parseFloat($("#current_answer").attr("value"));
    var ans = $('input[name="r"]:checked').val();


    if (ans < 0 || ans > 100) {
        alert("Неверный ввод!");
        return;
    }
    ExpertSystem.processAnswer(ans);
    ExpertSystem.nextStep();

}

function step_test() {
    //var ans = parseFloat($("#current_answer").attr("value"));
    var ans = $('input[name="r"]:checked').val();


    if (ans < 0 || ans > 100) {
        alert("Неверный ввод!");
        return;
    }
    ExpertSystem.processAnswer(ans);
    ExpertSystem.nextStep_test();

}

function init() {

    loadItemsFromLocalStorage();
    /**
     * Выбор теста. Его загрузка с localStorage, либо парсинг с textarea
     */
    $("#test1").val(baza);

    $("#start_test").bind("click keypress", function() {


        if ($(".b_page_test_switch__selected") && $(".b_page_test_switch__selected").length > 0) {
            ExpertSystem = loadFromLocalStorage($(".b_page_test_switch__selected").attr("index"));
        } else {
            ExpertSystem = new Test();
            if (!ExpertSystem.parseData($("#test").val())) {
                //if (!ExpertSystem.parseData($("#test1").val()))
                //{
                alert("Что-то пошло не так. Проверьте вводимые данные.")
                return;
                //}

            }

            saveToLocalStorage(ExpertSystem);
        }

        $("#test").addClass("hide");
        $(".b_page_test").removeClass("hide");
        $(".b_page_main").add("#start_test,#data_format,#inputFile,#data_load,#data_save,#testing").addClass("hide");
        //$("#test_title").html(ExpertSystem.title);
        $(".b_table").addClass("hide");
        $("#complete_answer_test").addClass("hide");
        $("#test_title").html("Выпускная квалификационная работа: Разработка экспертной системы «Домашний доктор» Студента 4 курса группы КБ-3 Манаширова Шарона Сионовича");


        ExpertSystem.nextStep();
    });

    $("#current_answer").bind('keydown ', function(e) {
        if (e.keyCode == 13) step();
    });
    $("#complete_answer").bind("click keypress", step);

    $("#testing").bind("click keypress", function() {

        if ($(".b_page_test_switch__selected") && $(".b_page_test_switch__selected").length > 0) {
            ExpertSystem = loadFromLocalStorage($(".b_page_test_switch__selected").attr("index"));
        } else {
            ExpertSystem = new Test();
            if (!ExpertSystem.parseData($("#test").val())) {
                //if (!ExpertSystem.parseData($("#test1").val()))
                //{
                alert("Что-то пошло не так. Проверьте вводимые данные.")
                return;
                //}


            }
            saveToLocalStorage(ExpertSystem);
        }

        $("#test").addClass("hide");
        $(".b_page_test").removeClass("hide");
        $(".b_page_main").add("#start_test,#data_format,#inputFile,#data_load,#data_save,#testing").addClass("hide");
        //$("#test_title").html(ExpertSystem.title);
        $(".b_page_diagnose").addClass("hide");
        $("#complete_answer").addClass("hide");
        $("#test_title").html("Выпускная квалификационная работа: Разработка экспертной системы «Домашний доктор» Студента 4 курса группы КБ-3 Манаширова Шарона Сионовича");


        ExpertSystem.nextStep_test();
    });

    $("#current_answer").bind('keydown ', function(e) {
        if (e.keyCode == 13) step_test();
    });
    $("#complete_answer_test").bind("click keypress", step_test);

    //$("#complete_answer_test").bind("click keypress", step);
    /**
     * визуализация выбора теста
     */
    $(".b_page_test_switch__item").live("click keypress", function() {
        if ($(this).hasClass("b_page_test_switch__selected")) {
            $(this).removeClass("b_page_test_switch__selected");
            return;
        }
        $(".b_page_test_switch__selected").removeClass("b_page_test_switch__selected");
        $(this).addClass("b_page_test_switch__selected");
    });

    $("#data_format").bind("click keypress", function() {
        $("#test").val(
            "Формат хранения данных:\n" +
            "На первой строке находится название базы знаний\n" +
            "На следующей через знак перевода строки располагается список вопросов\n" +
            "Далее через знак перевода строки располагается список событий (вариантов) в формате:\n" +
            "Событие-перевод строки-Начальная_вероятность_события номер_вопроса) вероятность_max вероятность_min перевод строки\n" +
            "Пример:\n" +
            "Определение пола\n" +
            "\n" +
            "Вы мужского пола?\n" +
            "Вы женского пола?\n" +
            "\n" +
            "Мужчина\n" +
            "0.5 1) 1 0 2) 0 1\n" +
            "Женщина\n" +
            "0.5 2) 1 0 1) 0 1\n" +
            "Номера вопросов можно устанавливать не по порядку, также можно опускать вопросы не влияющие на вероятность события");


    });

    $("#data_load").bind("click keypress", function() {
        $("#inputFile").click();
    });

    $("#data_save").bind("click keypress", function() {
        var blob = new Blob([test.value], { type: "text/plain;charset=utf-8" });
        saveAs(blob, "test.txt");
    });



    inputFile.onchange = function() {
        var file = inputFile.files[0];
        var reader = new FileReader;

        reader.onloadend = function(evt) {
            test.value = reader.result; // file content
        };

        reader.readAsText(file);
    };
}

window.onload = init;

function sortItems(a, b) {
    if (a.points > b.points || (a.points == b.points && a.title > b.title)) return 1;
    if (a.points == b.points && a.title == b.title) return 0;
    return -1;
}

function sortQuestion(a, b) {

    var aPoints = 0,
        bPoints = 0;
    for (var i = 0; i < a.items.length; i++) {

        aPoints += a.items[i].questionPoints[a.index].min + a.items[i].questionPoints[a.index].max + a.items[i].points;
    }
    for (var i = 0; i < b.items.length; i++) {
        bPoints += b.items[i].questionPoints[b.index].min + b.items[i].questionPoints[b.index].max + b.items[i].points;
    }

    if (aPoints > bPoints) return -1;
    if (aPoints == bPoints) {
        if (a.items.length > b.items.length) return -1;
        if (a.items.length == b.items.length) return 0;
    }
    return 1;
}

function Test(testObject) {

    this.title = "";
    this.items = [];
    this.questions = [];
    this.currentQuestion = -1;
    this.complete = false;
    if (testObject) {
        this.title = testObject.title;
        this.items = testObject.items;
        this.questions = testObject.questions;
    }
}

Test.prototype.stringify = function() {
    return JSON.stringify({
        title: this.title,
        items: this.items,
        questions: this.questions
    });
}

Test.prototype.printData = function() {
    this.items.sort(sortItems);
    //var template = '<div title="{0}: {1}" class="b_page_test_items__item border_radius"><span class="b_page_test_items__item_title">{0}</span><span class="b_page_test_items__item_percent">{1}</span></div>';
    var template = '<div title="{0}: {1}" class="b_page_test_items__item border_radius"><a href="text.html#{0}">{0}</a><span class=b_page_test_items__item_percent>{1}</span></div>';
    var t = $(".b_page_test_items");
    t.html("");

    for (var i = this.items.length - 1; i >= 0; i--) {
        var url = "text.html#" + this.items[i].title;
        var res = this.items[i].points > 1 ? 1 : this.items[i].points;
        t.html(t.html() + template.replace("{0}", this.items[i].title).replace("{0}", this.items[i].title).replace("{0}", this.items[i].title).replace("{1}", res).replace("{1}", res));
        if (res == 1) {
            this.complete = true;
        }
    }
}


Test.prototype.printData_test = function() {

    var template = '<div title="{0}: {1}" class="b_page_test_items__item_test border_radius"><span class="b_page_test_items__item_title">{0}</span><span class="b_page_test_items__item_percent">{1}</span></div>';
    var t = $(".b_page_test_items");
    t.html("");

    this.questions.sort(sortQuestion);

    //for(j=0;j<=0;j++) {
    $('#table').append('<tr><td>' + 'Вопрос ' + this.questions[0].q + " Ваш ответ: " + $('input[name="r"]:checked').attr("placeholder") + '</td>');

    for (i = 0; i <= this.items.length - 1; i++) {
        var res = this.items[i].points > 1 ? 1 : this.items[i].points;

        $('#table > tbody > tr:last').append('<td nowrap>' + (template.replace("{0}", this.items[i].title).replace("{0}", this.items[i].title).replace("{1}", res).replace("{1}", res)) + '</td>');
        if (res == 1) {
            this.complete = true;
        }
    }
    //$('#table').append('<tr> <td>'+'Ответ:'+$('input[name="r"]:checked').val()+'\n'+'Вопрос '+this.questions[0].q+'</td></tr>');
    //$('#table').append('<tr><td>'+'Вопрос '+this.questions[0].q+', '+$('input[name="r"]:checked').val()+'</tr></td>');

    //	}

}

Test.prototype.nextStep = function() {

    this.printData();
    this.questions.sort(sortQuestion);
    if (this.questions.length == 0 || this.complete) {
        $("#current_question").html("Ознакомьтесь с решением системы. Вопросы закончены.");
        $("#complete_answer").add("#current_answer").addClass("hide");
        return;
    }
    $("#current_question").html(this.questions[0].q);
    $("#current_answer").attr("value", '');
};

Test.prototype.nextStep_test = function() {

    this.printData_test();
    this.questions.sort(sortQuestion);
    if (this.questions.length == 0 || this.complete) {
        $("#current_question").html("Ознакомьтесь с решением системы. Вопросы закончены.");
        $("#complete_answer_test").add("#current_answer").addClass("hide");
        return;
    }
    $("#current_question").html(this.questions[0].q);
    $("#current_answer").attr("value", '');
};

Test.prototype.processAnswer = function(ans) {
    for (var i = 0; i < this.items.length; i++) {
        var point = this.items[i].questionPoints[this.questions[0].index];
        if (point) {
            var up = ((2 * point.max - 1) * ans / 100 + 1 - point.max) * this.items[i].points;
            var down = ((2 * point.max - 1) * ans / 100 + 1 - point.max) * this.items[i].points + ((2 * point.min - 1) * ans / 100 + 1 - point.min) * (1 - this.items[i].points);
            this.items[i].points = down != 0 ? up / down : this.items[i].points;
        }
    }
    var template = '<div class="b_page_questions__answers_item">{0}</div>'
    $("#answers").html($("#answers").html() + template.replace("{0}", this.questions[0].q + " Ваш ответ: " + $('input[name="r"]:checked').attr("placeholder")))
    this.questions.shift();
}

Test.prototype.parseData = function(data) {
    try {
        //Пропуск лишних, пустых строк
        var passEmptyStrings = function() {
            while (position < items.length && items[position] == "") { position++; }
        }

        var items = data.split("\n");
        var position = 0;
        passEmptyStrings();
        this.title = items[position++];
        passEmptyStrings();
        //Ввод вопросов
        while (items.length > position && items[position] != "") {
            this.questions.push({
                q: items[position++],
                items: [],
                index: this.questions.length
            });
        }
        if (items.length <= position) throw "Invalid data format";

        passEmptyStrings();

        var index = 0;
        //Ввод событий
        while (items.length > position && items[position] != "") {
            var pointItems = items[position + 1].split(" ");
            var newItem = {
                title: items[position],
                points: parseFloat(pointItems[0]),
                index: index,
                questionPoints: []
            };
            //Вероятности событий при 100 и 0% вероятностях ответа на вопрос
            for (var i = 1; i < pointItems.length; i += 3) {
                while (pointItems[i] == "") i++;
                var questionIndex = parseFloat(pointItems[i]) - 1;
                var questionPoint = {
                    max: parseFloat(pointItems[i + 1]),
                    min: parseFloat(pointItems[i + 2])
                };
                newItem.questionPoints[questionIndex] = questionPoint;

                this.questions[questionIndex].items.push(newItem);


            }

            this.items.push(newItem);
            index++;
            position += 2;
        }
        return true;
    } catch (e) {
        console.log(e);
        return false;
    }
}