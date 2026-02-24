#prompt #var #let #consolelog 
```TypeScript
let words: string[] = ["да", "нет","возможно","частично",];

let words_len = words.length;

let answer_index: number = Math.floor(Math.random() * words_len);

  

prompt()

console.log(words, words_len,answer_index)

alert(words[answer_index])

```

##### **let** и **var** для обозначения переменной.
##### **prompt** выводит строку ввода.

##### **console.log** вывод.

##### **TypeScript** 
Развивается TypeScript начал в 2012гг. Его разработкой занимался программист Андерс Хейлсберг. Он уже написал много известных прогарам(Delphi, C#).  

```TypeScript
function lengthOfLastWord(s: string): number {

    s = s.trim();

    let ls: number = s.lastIndexOf("");

    let ls2: string = s.slice(ls + 1);

    console.log(ls2);

    return ls2.length;

};

```

```TypeScript
function plusOne(digits: number[]): number[] {

  

    if (digits.length = 1) {

        if (digits[0] < 9) {

            digits[0] +=1;

        }

    }

  

    for (let i = digits.length;i > 0 ; i--)

        if (digits[i] < 9) {

            digits[i] += 1;

  

            break;

        }

        else {

            digits[i] == 0 ;

  

    };

    return digits

};
```