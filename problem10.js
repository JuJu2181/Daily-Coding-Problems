const f = () => console.log("Function Called");
let n = 500

const jobScheduler = (f, n) => {
    setTimeout(f, n);
}

jobScheduler(f, n);