//% color=#6d5ba4 icon="\uf0f2"
namespace bundles{
    /**
    * just run the code
    */
    //% block="create player 1"  weight=300
    //% handlerStatement=1
    export function wrap1(handler: () => void) {
        handler();
    }
    /**
    * just run the code
    */
    //% block="create player 2"  weight=200
    //% handlerStatement=1
    export function wrap2(handler: () => void) {
        handler();
    }
    /**
    * just run the code
    */
    //% block="create arrow"  weight=100
    //% handlerStatement=1
    export function wrap3(handler: () => void) {
        handler();
    }
    /**
    * just run the code
    */
    //% block="finishing touches"
    //% handlerStatement=1
    export function wrap4(handler: () => void) {
        handler();
    }
}