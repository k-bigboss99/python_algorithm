# Python Algorithm
## CH2 Array

- 陣列 Array
    - 資料是放在連續的記憶體空間，使用index存取

- 缺點
    - 連續的記憶體空間，可能會有記憶體不足的問題，須將array整體移動至新的記憶體區
        - 解決方法:
            - 預設更多的記憶體空間，但可寧造成記憶體空間的浪費

- List vs Array
    - List 串列架構允許陣列元素含有不同資料型態，但也會造成執行速度較差與較多的系統資源
    - 資料量少 可以將List當作Array使用

- Python 內建Array模組，可用type code指定陣列的資料型態
    - `array(typecode,[陣列內容])`
    ![](https://i.imgur.com/euhZCwa.png)
    
- Numpy

## CH3 Linked List
- 鏈結串列 Listed List
    - 元素是散佈在記憶體的各個地方
    - 讀取資料使用sequential access ，搜尋資料必須重頭開始搜尋資料
    - 節點分為兩區域:資料區、指標區

- Single Listed List
    - 指標區指向下一個節點元素
    - 只能往後搜尋

- Double Listed List
    - 兩個指標區，1.指向前一個節點 2.指向後一個節點
    - 可以往前往後搜尋

