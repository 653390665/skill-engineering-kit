Architecture Decision：不要因为有四个角色就机械拆成四个 skill。

判断依据应是 workflow、agent、shared 资源和触发边界。

如果产品、技术、商业、风险只是同一流程中的视角，应放在一个 skill 的 agents 或 prompts 下；只有触发、输入、输出、生命周期明显不同，才拆分。
