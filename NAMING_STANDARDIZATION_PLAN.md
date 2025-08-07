# Repository Naming Standardization Plan

## 🎯 **Standardization Goal**

Convert all repository names to **kebab-case** for consistency and professional appearance on GitHub.

**Standard**: `project-name-with-description`

## 📊 **Current Repository Analysis**

### **Total Repositories**: 42

### **Current Naming Patterns:**
- **PascalCase**: 15 repositories
- **snake_case**: 10 repositories  
- **kebab-case**: 12 repositories
- **camelCase**: 4 repositories
- **Mixed/Inconsistent**: 1 repository

## 🔄 **Standardization Plan**

### **Phase 1: High Priority Repositories (Already Professionalized)**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `AI_Debugger_Assistant` | `ai-debugger-assistant` | AI/ML | High | 🔄 Ready |
| `bolt-project` | `dreamforge-ai-agent` | AI/ML | High | 🔄 Ready |
| `agentproject` | `code-refactoring-automation` | Development | High | 🔄 Ready |
| `FreeWork` | `freemail-management` | Productivity | High | 🔄 Ready |
| `FocusForge` | `focus-forge` | Productivity | High | 🔄 Ready |
| `DreamVault` | `dream-vault` | AI/ML | High | 🔄 Ready |

### **Phase 2: Trading & Financial Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `FreeRideInvestor` | `free-ride-investor` | Trading | High | 🔄 Ready |
| `SmartStock-pro` | `smart-stock-pro` | Trading | High | 🔄 Ready |
| `trading-leads-bot` | `trading-leads-bot` | Trading | High | ✅ Already kebab-case |
| `TradingRobotPlug` | `trading-robot-plug` | Trading | High | 🔄 Ready |
| `TradingRobotPlugWeb` | `trading-robot-plug-web` | Trading | High | 🔄 Ready |
| `TRPlugLibrary` | `tr-plug-library` | Trading | High | 🔄 Ready |
| `ultimate_trading_intelligence` | `ultimate-trading-intelligence` | Trading | High | 🔄 Ready |
| `UltimateOptionsTradingRobot` | `ultimate-options-trading-robot` | Trading | High | 🔄 Ready |

### **Phase 3: AI & Machine Learning Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `gpt_automation` | `gpt-automation` | AI/ML | Medium | 🔄 Ready |
| `LSTMmodel_trainer` | `lstm-model-trainer` | AI/ML | Medium | 🔄 Ready |
| `machinelearningmodelmaker` | `machine-learning-model-maker` | AI/ML | Medium | 🔄 Ready |
| `machinelearningproject` | `machine-learning-project` | AI/ML | Medium | 🔄 Ready |
| `osrsAIagent` | `osrs-ai-agent` | AI/ML | Medium | 🔄 Ready |
| `osrsbot` | `osrs-bot` | AI/ML | Medium | 🔄 Ready |
| `self-evolving-ai` | `self-evolving-ai` | AI/ML | Medium | ✅ Already kebab-case |

### **Phase 4: Development & Utility Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `basicbot` | `basic-bot` | Development | Medium | 🔄 Ready |
| `content` | `content` | Content | Low | ✅ Already kebab-case |
| `ideas` | `project-ideas` | Development | Medium | ✅ Completed |
| `practice` | `practice-projects` | Development | Low | 🔄 Ready |
| `projectscanner` | `project-scanner` | Development | Medium | 🔄 Ready |
| `network-scanner` | `network-scanner` | Development | Medium | ✅ Already kebab-case |
| `socialmediamanager` | `social-media-manager` | Development | Medium | 🔄 Ready |

### **Phase 5: Personal & Portfolio Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `DaDudekC` | `dadudekc` | Personal | Low | 🔄 Ready |
| `DaDudeKC-Website` | `dadudekc-website` | Personal | Low | 🔄 Ready |
| `my-personal-templates` | `my-personal-templates` | Personal | Low | ✅ Already kebab-case |
| `my-resume` | `my-resume` | Personal | Low | ✅ Already kebab-case |
| `Resume-Showcase` | `resume-showcase` | Personal | Low | 🔄 Ready |
| `prompt-library` | `prompt-library` | Personal | Low | ✅ Already kebab-case |

### **Phase 6: Gaming & Entertainment Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `NewSims4ModProject` | `sims4-mod-project` | Gaming | Low | 🔄 Ready |
| `tbow-tactics` | `tbow-tactics` | Gaming | Low | ✅ Already kebab-case |

### **Phase 7: Other Projects**

| Current Name | Proposed Name | Category | Priority | Status |
|--------------|---------------|----------|----------|--------|
| `DigitalDreamscape` | `digital-dreamscape` | Creative | Low | 🔄 Ready |
| `Hive-Mind` | `hive-mind` | Creative | Low | 🔄 Ready |
| `Hive-Mind` | `hive-mind` | Creative | Low | 🔄 Ready |
| `IT_help_desk` | `it-help-desk` | Support | Medium | 🔄 Ready |
| `MeTuber` | `me-tuber` | Social | Low | 🔄 Ready |
| `Side-projects` | `side-projects` | Development | Low | ✅ Already kebab-case |
| `TROOP` | `troop` | Development | Low | 🔄 Ready |

## 🚀 **Implementation Strategy**

### **Step 1: Create Backup**
```bash
# Create backup of current structure
cp -r Dadudekc Dadudekc_backup_$(date +%Y%m%d)
```

### **Step 2: Rename High Priority Repositories**
```bash
# Phase 1: Already professionalized repositories
mv AI_Debugger_Assistant ai-debugger-assistant
mv bolt-project dreamforge-ai-agent
mv agentproject code-refactoring-automation
mv FreeWork freemail-management
mv FocusForge focus-forge
mv DreamVault dream-vault
```

### **Step 3: Update References**
- Update all README.md files that reference other repositories
- Update any hardcoded paths in scripts
- Update documentation links

### **Step 4: Create Naming Guidelines**
- Document the kebab-case standard
- Create naming conventions for future projects
- Add to project templates

## 📋 **Action Items**

### **Immediate Actions (Phase 1)**
- [ ] Backup current repository structure
- [ ] Rename 6 high-priority repositories
- [ ] Update README references in professionalized projects
- [ ] Test functionality after renaming

### **Secondary Actions (Phase 2-7)**
- [ ] Rename remaining 36 repositories
- [ ] Update all cross-references
- [ ] Create naming convention documentation
- [ ] Update project templates

## ⚠️ **Risk Assessment**

### **High Risk:**
- **Broken references** in README files
- **Hardcoded paths** in scripts
- **Git history** preservation

### **Mitigation Strategies:**
- Create comprehensive backup before starting
- Test each rename individually
- Update all references immediately after rename
- Use git mv for proper history preservation

## 📊 **Success Metrics**

### **Target:**
- **100% kebab-case** naming (42/42 repositories)
- **0 broken references** in documentation
- **Consistent naming** across all projects
- **Professional appearance** on GitHub

### **Current Status:**
- **12/42** repositories already in kebab-case (29%)
- **30/42** repositories need renaming (71%)

---

**Ready to begin Phase 1 renaming?** 🚀
