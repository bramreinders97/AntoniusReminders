### Load Environment Variables
**Load Antonius environment (default):**
```powershell
.\set_env.ps1
```

**Load Goudenregen environment:**
```powershell
.\set_env.ps1 -EnvFile .env.goudenregen
```

### Run tests
**Load Antonius environment (default):**
```python tests/test_specific_date.py```

OR 

```python tests/test_next_30_days.py```
