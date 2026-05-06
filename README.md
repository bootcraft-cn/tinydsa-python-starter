# TinyDSA Starter — Python

TinyDSA 课程起始代码（Python）——从零手搓经典数据结构与算法。

## 结构

```
tinydsa/           # 核心实现（所有数据结构累积在此）
tests/             # 每个 stage 一个测试 (test_s01 … test_s17)
tinycs.yml      # 课程元数据
```

## 开始

在 `tinydsa/` 目录下找到 `TODO` 注释，按 stage 顺序逐步实现。

## 规则

- **禁止使用** Python 内置的 `list.append()`、`list.insert()`、`list.pop()` 等动态方法
- 底层存储必须使用 `[None] * capacity` 固定长度数组
- 测试文件（`tests/`）请勿修改
