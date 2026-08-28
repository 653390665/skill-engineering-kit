不能算通过。

这是 contaminated run：测试 agent 已经看过 grading-card 和正确答案，结果会被污染。

处理方式：re-run。重新生成隔离任务，只给 task，不给 grading-card。
