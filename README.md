# Zerojudge Stats Badge

## 在靜態網頁中顯示使用者當前的Zerojudge解題統計！

可以在Github Profile顯示當前Zerojudge的解題紀錄！
<!-- ![](https://i.imgur.com/FXJaYDb.png) -->
<img src="https://i.imgur.com/FXJaYDb.png" width="500" height="350" />

目前是**Beta版本**，會再進行調整、完善界面跟主題。
### 使用方法：

```
[![Zerojudge Stats](https://zj-query-0.herokuapp.com/user?user_id=122857&name=Jason)](https://github.com/jason810496/Zerojudge-stats)
```

將其中的`user_id`改成[`Zerojudge`](https://zerojudge.tw/)帳號的ID

而`name`是左上想要顯示的使用者名稱

現在的結果：(根據現在server的狀態有所不同，而以下其他的圖片則是事先截圖好的)

[![Zerojudge Stats](https://zj-query-0.herokuapp.com/user?user_id=122857&name=Jason&theme=blux)](https://github.com/jason810496/Zerojudge-stats)

**如何知道自己帳號的ID ?**

先到Zerojudge首頁右側的選單，前往自己的user information

<!-- ![ZJ nav](https://i.imgur.com/2D4wdp2.png) -->

<img src="https://i.imgur.com/2D4wdp2.png" width="200" height="210" />

在自己的統計頁面左側可以找到ID

<!-- ![ID](https://i.imgur.com/K7hZfEC.png) -->
<img src="https://i.imgur.com/K7hZfEC.png" width="200" height="250" />

成功的結果：

![success](https://i.imgur.com/dn4aFHP.png)

### 參數：
| 參數      | 功能               | 預設 |
| --------- | ------------------ | ---- |
| `user_id` | 查詢使用者資料     |  `0`    |
| `name`    | 在左上角顯示的名稱 |  `User`    |
| `theme`          |         主題顏色           | `default`     |

如：[主題](https://github.com/jason810496/Zerojudge-stats/tree/master/theme)選用`react`、使用者ID為`123`、顯示名稱是`JoJo`：
```
![Zerojudge Stats](https://zj-query-0.herokuapp.com/user?user_id=123&name=JoJo&theme=react)
```

未來會加入的參數：
- `font`
- `border`
- `width`
- `height`

如果有其他需求可以發issue!

### 主題顏色：

目前有**18種**主題：
[目前有的主題配色](https://github.com/jason810496/Zerojudge-stats/tree/master/theme)
### 錯誤警示：
錯誤ID：


![404](https://i.imgur.com/7OUquaA.png)

Server錯誤：


![500](https://i.imgur.com/wZwhp1m.png)


(可能是連不到Zerojudge或是該系統的問題 )

### 有關延遲＆一直都是Server錯誤：
- **延遲**

目前的server是部屬在Heroku(他們的主機在美國)，也就是要在網站顯示資料必須**來回傳送4次**，也要根據當前的網路狀況，所以有所延遲。

`瀏覽者`→ `my server`→ `Zerojudge`→ `my server` →`瀏覽者`

而多數的瀏覽者都在台灣，所以未來會考慮自架server，或選擇在台灣有主機的cloud server。

- **都是Server錯誤**

如果一直都是Server Error，可以登入到Zerojudge看看。如果也連不到Zerojudge，那代表有可能Zerojudge暫時下線、維修等。

如果連的到Zerojudge，那代表應該是我這邊的問題，需要我這邊重新登錄(原因可以看下方實做細節的[連結](https://jason810496.github.io/blog/2022-03-24-ZJstats0/))，可以直接通知我！


### 實做細節：

發布於[My blog](https://jason810496.github.io/blog/2022-03-24-ZJstats0/)

### 參考資料：

[Github readme stats](https://github.com/DenverCoder1/github-readme-streak-stats)



