# Azure Static Web Apps Deployment Guide

## Prerequisites
- Azure account with active subscription
- GitHub account
- Git repository with your code (already done ✓)

## Deployment Steps

### Option 1: Deploy via Azure Portal (Recommended)

1. **Go to Azure Portal**
   - Navigate to https://portal.azure.com

2. **Create Static Web App**
   - Click "Create a resource"
   - Search for "Static Web Apps"
   - Click "Create"

3. **Configure Basic Settings**
   - **Subscription**: Select your Azure subscription
   - **Resource Group**: Create new or use existing
   - **Name**: `bleak-house-tracker` (or your preferred name)
   - **Plan type**: Free (perfect for this app)
   - **Region**: Choose closest to you

4. **Configure GitHub Integration**
   - **Source**: GitHub
   - Click "Sign in with GitHub" and authorize
   - **Organization**: Your GitHub username
   - **Repository**: Select your BleakHouseAssist repo
   - **Branch**: master

5. **Build Configuration**
   - **Build Presets**: Custom
   - **App location**: `/`
   - **Api location**: (leave empty)
   - **Output location**: (leave empty)

6. **Review + Create**
   - Click "Review + create"
   - Click "Create"

7. **Wait for Deployment**
   - Azure will automatically:
     - Add GitHub Actions workflow to your repo
     - Build and deploy your app
     - Provide you with a URL

### Option 2: Deploy via Azure CLI

```bash
# Login to Azure
az login

# Create resource group
az group create --name bleak-house-rg --location eastus

# Create static web app
az staticwebapp create \
  --name bleak-house-tracker \
  --resource-group bleak-house-rg \
  --source https://github.com/YOUR_USERNAME/BleakHouseAssist \
  --branch master \
  --app-location "/" \
  --output-location "" \
  --login-with-github
```

## Post-Deployment

### Your App Will Be Available At:
`https://bleak-house-tracker.azurestaticapps.net`
(or similar URL based on your chosen name)

### GitHub Actions
- Workflow automatically added to `.github/workflows/`
- Deploys on every push to master
- Check Actions tab in GitHub to monitor deployments

### Custom Domain (Optional)
1. In Azure Portal, go to your Static Web App
2. Click "Custom domains"
3. Add your domain and follow DNS configuration steps

## Configuration Files Included

✓ **staticwebapp.config.json** - Static Web App configuration
✓ **.github/workflows/azure-static-web-apps.yml** - GitHub Actions workflow

## Features Enabled

- ✓ Automatic deployment on git push
- ✓ Pull request preview environments
- ✓ Free SSL certificate
- ✓ Global CDN distribution
- ✓ Custom domains support
- ✓ Free hosting (up to 100GB bandwidth/month)

## Troubleshooting

### If deployment fails:
1. Check GitHub Actions tab for error details
2. Verify staticwebapp.config.json is valid JSON
3. Ensure all required files are committed

### If app doesn't load:
1. Check that index.html is in root directory
2. Verify data.js is being served correctly
3. Check browser console for errors

## Cost
**FREE** on the Free tier, which includes:
- 100 GB bandwidth per month
- 0.5 GB storage
- 2 custom domains
- Free SSL certificates

Perfect for this application!

## Next Steps After Deployment

1. **Test the deployed app** at your Azure URL
2. **Update README.md** with the live URL
3. **Share with users** - it's now publicly accessible!
4. **Monitor usage** in Azure Portal metrics

## Support
- Azure Static Web Apps docs: https://docs.microsoft.com/azure/static-web-apps/
- GitHub Actions docs: https://docs.github.com/actions
