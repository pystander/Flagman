function controlCar(scanArray) {
    var maxi = scanArray[0];
    var idx = 0;
    for (let i = 1; i <= 16; i++) {
        if (scanArray[i] >= maxi) {
            maxi = scanArray[i];
            idx = i - 1;
        }
    }

    if (idx == 8) {
        return 0;
    } else if (idx < 8) {
        return -1;
    } else {
        return 1;
    }
}