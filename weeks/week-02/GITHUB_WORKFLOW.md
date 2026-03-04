# Week 02：下週會用到的 GitHub 觀念與操作指令

> 本課程採 **不使用 GitHub Classroom** 的進階流程：
> `Template repo + upstream 同步 + 固定作業路徑 + 每週 branch + PR`

---

## 1) 核心觀念（先理解）

- `origin`：你自己的作業 repo（你 push 的地方）
- `upstream`：老師的教材 repo（你同步教材的來源）
- 每週作業用獨立分支（例如 `submit/week-03`）
- 作業只放在：`weeks/week-XX/solutions/<student-id>/`

---

## 2) 第一次設定 upstream（只做一次）

```bash
git remote add upstream https://github.com/DevSecOpsLab-CSIE-NPU/2026-python.git
git remote -v
```

確認有兩個 remote：

- `origin`（你的 repo）
- `upstream`（課程 repo）

---

## 3) 每次上課前同步教材

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

> 規範：同步前先 commit 自己的改動，避免 merge 時把未完成變更混在一起。

---

## 4) 每週提交（branch + PR）

以 week-03 為例：

```bash
git checkout -b submit/week-03
# 在 weeks/week-03/solutions/<student-id>/ 撰寫解答
git add .
git commit -m "Submit week-03"
git push origin submit/week-03
```

到 GitHub 開 PR：

- base：`main`
- compare：`submit/week-03`
- PR 標題：`Week 03 - <student-id> - <name>`

範例：

```text
Week 03 - 411234001 - 王小明
```

---

## 5) 允許與禁止修改路徑

### ✅ 只允許提交

```text
weeks/week-XX/solutions/<student-id>/
```

### ❌ 禁止修改

- `weeks/week-XX/QUESTION-*.md`
- `weeks/week-XX/README.md`
- `docs/*`（除非老師公告允許）

---

## 6) PR 描述建議模板

```markdown
## 完成題號
- QUESTION-100
- QUESTION-118

## 執行方式
- python3 solution.py < input.txt

## 依賴套件
- 無

## 補充說明
- 目前已通過基本測資
```

---

## 7) 評分與改分機制（你需要知道）

- 助教會在 PR Review 留分數與建議
- 若後續修正而改分，會以「更新留言」保留紀錄
- 正式成績以 LMS/成績表為準，PR 留言作為追溯依據

---

## 8) 常用 Git 指令速查

```bash
# 看目前分支與狀態
git branch
git status

# 看尚未提交的差異
git diff

# 看提交紀錄
git log --oneline --decorate -n 10

# 分支推上去並設定追蹤
git push -u origin submit/week-03
```

---

## 9) 提交前檢查清單

- [ ] 已先同步 `upstream/main`
- [ ] 只改到 `solutions/<student-id>/`
- [ ] 分支名稱是 `submit/week-XX`
- [ ] PR 標題符合格式
- [ ] PR 描述包含題號、執行方式、依賴

---

## 延伸閱讀

- 學生版完整指南：`docs/SUBMISSION_GUIDE.md`
- 助教評分規範：`docs/TA_GRADING_GUIDE.md`
- PR 規範檢查工作流：`.github/workflows/submission-policy-check.yml`
