# Python Algorithm

- [環境安裝](https://segmentfault.com/a/1190000005087181)
- [Matplotlib](https://www.runoob.com/numpy/numpy-matplotlib.html)
## CH1 演算法基本觀念

- 演算法特徵
    - 輸入:一個演算法必須有0個 or 更多的輸入
    - 有限性:一個演算法的步驟必須是有限的步驟
    - 明確性:演算法描述必須是明確的
    - 有效性:演算法的可行性可以獲得正確的執行結果
    - 輸出:計算結果，一個演算法都必須有一個以上的輸出

-  eval() 函數用來執行一個字符串表達式，並返回表達式的值
    - `eval （表達式[，globals [，locals ]]）`
        - expression -- 表達式。
        - globals -- 變量作用域，全局命名空間，如果被提供，則必須是一個字典對象。
        - locals -- 變量作用域，局部命名空間，如果被提供，可以是任何映射對象

- Python 內建 itertools 模組，此模組內有 permuations()，舉列出所有元素排列組合

- Python 內建 math 模組，此模組可用來運算 log 值
    - `math.log(x[,base])` , base 為底數，預設為 e = 2.718281828459
    - 也可使用 log2()、log10()

- Numpy 中的 linspace 函數可以在一定範圍內來均勻地撒點
    - `np.linspace(起始點, 結束點, 個數) `
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

- Python 內建 Array 模組，可用 type code 指定陣列的資料型態
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

