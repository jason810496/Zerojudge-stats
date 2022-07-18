# Zerojudge Stats Badge

## 在靜態網頁中顯示使用者當前的Zerojudge解題統計！

可以在Github Profile顯示當前Zerojudge的解題紀錄！
<!-- ![](https://i.imgur.com/FXJaYDb.png) -->
<img src="https://i.imgur.com/FXJaYDb.png" width="500" height="350" />

目前是**1.0版本**，主要的問題已解決，可能還會針對細節做微調。
### 使用方法：

```
[![Zerojudge Stats](https://zj-query-0.herokuapp.com/user?account=AccountName&name=Jason)](https://github.com/jason810496/Zerojudge-stats)
```

將其中的`AccountName`改成[`Zerojudge`](https://zerojudge.tw/)的帳號

而`name`是左上想要顯示的使用者名稱

現在的結果：(根據現在server的狀態有所不同，而以下其他的圖片則是事先截圖好的)

[![Zerojudge Stats](https://zj-query-0.herokuapp.com/user?account=810496@email.wlsh.tyc.edu.tw&name=Jason&theme=blux)](https://github.com/jason810496/Zerojudge-stats)


**如果是 Google 登入怎麼辦 ?**

那就是註冊 Zerojudge 的 Google 帳號 

如果不確定的話 ，可以先到 Zerojudge 首頁右側的選單，前往自己的user information

<!-- ![ZJ nav](https://i.imgur.com/2D4wdp2.png) -->

<img src="https://i.imgur.com/2D4wdp2.png" width="200" height="210" />

在自己的統計頁面左側可以確定自己的帳號

<!-- ![ID](https://i.imgur.com/K7hZfEC.png) -->
<img src="https://i.imgur.com/K7hZfEC.png" width="200" height="250" />

( 以這個為例： `AccountName` 是 `810496@email.wlsh.tyc.edu.tw` )

成功的結果：

![success](https://i.imgur.com/dn4aFHP.png)

### 參數：
| 參數      | 功能               | 預設 |
| --------- | ------------------ | ---- |
| `Account` | 查詢使用者資料     |  **這是必填**   |
| `name`    | 在左上角顯示的名稱 |  `User`    |
| [`theme`](https://github.com/jason810496/Zerojudge-stats/tree/master/theme)          |         主題顏色           | `default`     |

如：[主題](https://github.com/jason810496/Zerojudge-stats/tree/master/theme)選用`react`、Account 為`123`、顯示名稱是`JoJo`：
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
錯誤 Account ：

![404](https://i.imgur.com/7OUquaA.png)


### 實做細節：

發布於[My blog](https://jason810496.codes/blog/2022/03/24/ZJstats0/)

( [Beta 版本實做細節](https://jason810496.codes/blog/2022/03/24/ZJstats0/)

### 參考資料：

[Github readme stats](https://github.com/DenverCoder1/github-readme-streak-stats)



