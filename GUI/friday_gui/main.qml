import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: window
    width: 1000
    height: 500
    visible: true
    color: "#00000000"
    title: qsTr("mainWindow")

    Rectangle {
        id: background
        color: "#5b5b5b"
        border.color: "#6d6d6d"
        border.width: 2
        anchors.fill: parent
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10

        Rectangle {
            id: container1
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 2
            anchors.leftMargin: 2
            anchors.bottomMargin: 2
            anchors.topMargin: 2

            Rectangle {
                id: topBar
                height: 81
                color: "#414141"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                Rectangle {
                    id: titleBar
                    visible: true
                    color: "#00000000"
                    anchors.fill: parent
                    anchors.rightMargin: 141
                    anchors.bottomMargin: 52

                    Label {
                        id: label
                        x: 47
                        y: 0
                        width: 785
                        height: 28
                        color: "#fdfdfd"
                        text: qsTr("F  R  I  D  A  Y ")
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.wordSpacing: 0
                        font.underline: false
                        font.italic: true
                        font.bold: true
                        font.family: "Verdana"
                        font.pointSize: 10
                    }

                    Image {
                        id: image
                        anchors.left: parent.left
                        anchors.right: label.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        anchors.rightMargin: 0
                        asynchronous: false
                        fillMode: Image.PreserveAspectFit
                    }
                }
            }

            Rectangle {
                id: sideBarContainer
                width: 78
                color: "#00000000"
                anchors.left: parent.left
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0

                Rectangle {
                    id: sideBar
                    color: "#414141"
                    anchors.fill: parent
                }
            }

            Rectangle {
                id: pageContainer
                color: "#00000000"
                anchors.left: sideBarContainer.right
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0

                Rectangle {
                    id: rectangle
                    color: "#5b5b5b"
                    anchors.fill: parent
                    anchors.topMargin: 0
                    anchors.leftMargin: 0
                }
            }
        }
    }
}
