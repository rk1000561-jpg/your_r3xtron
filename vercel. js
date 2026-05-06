{
  "version": 2,
  "builds": [
    {
      "src": "index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/bgmi/(.*)",
      "dest": "index.py"
    },
    {
      "src": "/(.*)",
      "dest": "index.py"
    }
  ]
}
