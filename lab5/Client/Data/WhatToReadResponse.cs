using System;
using System.Collections.Generic;

namespace Client.Data
{
    public class WhatToReadResponse : IResponce
    {
        public List<string> KeyWords { get; set; }

        private List<string> _ideas;

        public WhatToReadResponse()
        {
            KeyWords = new List<string>();
            _ideas = new List<string>()
            {
                "\"Властелин колец\", Джон Р. Р. Толкин",
                "\"Автостопом по галактике\", Дуглас Адамс",
                "\"1984\", Джордж Оруэлл",
                "\"Дюна\", Фрэнк Герберт",
                "\"Крёстный отец\", Марио Пьюзо",
                "\"Оно\", Стивен Кинг"
            };
        }

        public string GetResponce(string request)
        {
            foreach (string word in KeyWords)
                if (request.IndexOf(word) != -1)
                    return GetIdea();
            return null;
        }

        private string GetIdea()
        {
            string idea = "Что можно почитать: ";
            Random rnd = new Random();
            int index = (int)rnd.Next(0,_ideas.Count - 1);
            idea += _ideas[index];
            return idea;
        }
    }
}