# Hunt Stack Overflow enthusiast and fanatic badges automatically

Add in a daily cron job the execution of the self-contained Docker image:

```sh
docker run --rm -e EMAIL=<YOUR_STACKOVERFLOW_EMAIL> -e PASSWORD=<YOUR_STACKOVERFLOW_PASSWORD> jesugmz/stackoverflow-enthusiast-fanatic-badges
```

todo: add more documentation.
