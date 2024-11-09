"use client";
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Button } from "@/components/ui/button";
import { Download, InfoIcon } from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import Link from "next/link";
import { useState } from "react";

const PetsWithPagination = ({ rows }: { rows: any[] }) => {
  const itemsPerPage = 5;

  // حالة لتخزين عدد السجلات التي سيتم عرضها
  const [visibleRows, setVisibleRows] = useState(rows.slice(0, itemsPerPage));

  // دالة لعرض المزيد من السجلات عند الضغط على زر "عرض المزيد"
  const showMore = () => {
    const nextRows = rows.slice(0, visibleRows.length + itemsPerPage);
    setVisibleRows(nextRows);
  };

  return (
    <div className="flex flex-col gap-3">
      {visibleRows.length > 0 ? (
        visibleRows.map((font: any, index) => (
          <div
            key={index}
            className={`w-full relative flex flex-col gap-5 bg-primary-foreground border-none rounded-xl p-7 text-right text-nowrap`}
          >
            <Link
              href={`/${font?.id}`}
              className={`absolute top-0 bottom-0 left-0 right-0 w-full h-full rounded-3xl -z-0`}
              ria-label={`link view` + font?.id}
              aria-label={`link view` + font?.id}
              tabIndex={font?.id}
            ></Link>
            <p
              className={`text-5xl py-4 w-full -z-0 line-clamp-1 outline-none`}
              dir="rtl"
              contentEditable
            >
              {font.description}
            </p>
            <div className={`flex justify-between items-center z-0`}>
              <div className={`flex gap-2`}>
                <Dialog>
                  <DialogTrigger
                    className="bg-secondary rounded-full p-2.5"
                    aria-label={`Info icon` + font?.id}
                  >
                    <InfoIcon size={20} />
                  </DialogTrigger>
                  <DialogContent className="border-none bg-secondary">
                    <DialogHeader dir="rtl">
                      <DialogTitle>{font.name}</DialogTitle>
                      <DialogDescription
                        className={`text-2xl p-2 w-full`}
                        dir="rtl"
                      >
                        <p dir="rtl" className="text-right">
                          {font.info}
                        </p>
                        <p dir="rtl" className="text-right">
                          {font.tags}
                        </p>
                        <p dir="rtl" className="text-left text-base">
                          {font.created_at.toString()}
                        </p>
                        <p dir="rtl" className="text-left text-base">
                          {font.more}
                        </p>
                      </DialogDescription>
                    </DialogHeader>
                  </DialogContent>
                </Dialog>
                <Link href={`/${font?.id}`}>
                  <Button
                    variant={"secondary"}
                    size={"default"}
                    className="rounded-2xl"
                    aria-label={`Download icon` + font?.id}
                  >
                    <Download /> <span className="max-sm:hidden">Download</span>
                  </Button>
                </Link>
              </div>
              <Link href={`/${font?.id}`} className="text-base -z-5">
                {font.name}
              </Link>
            </div>
          </div>
        ))
      ) : (
        <span>لا توجد حيوانات أليفة في النظام.</span>
      )}

      {/* عرض زر "عرض المزيد" إذا كان هناك المزيد من السجلات */}
      {visibleRows.length < rows.length && (
        <Button variant={"outline"} size={"lg"} onClick={showMore}>
          عرض المزيد من الخطوط
        </Button>
      )}
    </div>
  );
};

export default PetsWithPagination;
