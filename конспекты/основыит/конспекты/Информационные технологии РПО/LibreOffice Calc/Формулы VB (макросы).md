Макросы в LibreOffice пишутся на языке LibreOffice Basic, но программа также поддерживает множество функций VBA (Visual Basic for Applications) для совместимости с документами Microsoft Office.
Как открыть редактор макросов

- Нажмите комбинацию клавиш `Alt + F11` или выберите в меню: **Сервис** -> **Макросы** -> **Управление макросами** -> **LibreOffice Basic**.

- Выберите нужный документ или «Мои макросы», нажмите **Править** или **Создать**.

Поддержка VBA

- В начале модуля VBA-макросов часто пишется директива `Option VBASupport 1`, которая включает совместимость с функциями Visual Basic for Applications.

- Поддерживаются стандартные функции работы со строками, датами (`DateAdd`, `DateDiff`) и математические операторы VBA.

- Официальный список поддерживаемых функций VBA смотрите в Справке LibreOffice.
Пример простейшего макроса для Calc

basic

```
Sub Main
    Dim oSheet As Object
    Dim oCell As Object
    ' Получаем текущий лист
    oSheet = ThisComponent.CurrentController.ActiveSheet
    ' Получаем ячейку A1 и пишем в нее текст
    oCell = oSheet.getCellByPosition(0, 0)
    oCell.String = "Привет, мир!"
End Sub
```