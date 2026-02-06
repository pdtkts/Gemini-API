# Git Fork Workflow

Hướng dẫn flow chuẩn khi làm việc với forked repository.

## Flow Chuẩn

### 1. Trước khi bắt đầu feature mới - Sync upstream

```bash
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

### 2. Tạo branch cho feature

```bash
git checkout -b feature/ten-tinh-nang
```

### 3. Code & Commit thường xuyên

```bash
git add .
git commit -m "feat: mô tả ngắn"
```

### 4. Push lên fork

```bash
git push origin feature/ten-tinh-nang
```

### 5. Khi xong - Merge vào master của bạn

```bash
git checkout master
git merge feature/ten-tinh-nang
git push origin master
```

### 6. (Optional) Tạo PR về upstream nếu muốn contribute

Vào GitHub → Create Pull Request từ `your-username:feature/xxx` → `original-owner:master`

## Lưu ý

- **origin**: Fork của bạn
- **upstream**: Repo gốc
- Luôn sync upstream trước khi tạo feature mới để tránh conflict
- Commit thường xuyên với message rõ ràng theo conventional commits
